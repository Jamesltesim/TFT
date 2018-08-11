
#!/usr/bin/env python


# https://www.cnblogs.com/yiwangzhibujian/p/7047458.html
# 一、单节点实例
# 二、主从模式（master/slaver）
# 三、sentinel模式
# 四、cluster模式



# 项目中用到Redis，所以准备学习一下，感觉Redis的概念还是很多的，什么主从模式、sentinel模式、集群模式的，一下子都晕了，我觉得还是有必要先理清这些基本概念再说。
#
# 一、单节点实例
# 　　单节点实例还是比较简单的，平时做个测试，写个小程序如果需要用到缓存的话，启动一个Redis还是很轻松的，做为一个key/value数据库也是可以胜任的。单节点部署参照：http://www.cnblogs.com/yiwangzhibujian/p/7053840.html 中的初级教程。
#
# 二、主从模式（master/slaver）
# 　　主从模式的简介和配置，此处不再说，参照下面的博客：Redis 主从模式详解。
#
# 　　首先谈谈我对主从模式的必要性：
#
# 主从模式的一个作用是备份数据，这样当一个节点损坏（指不可恢复的硬件损坏）时，数据因为有备份，可以方便恢复。
# 另一个作用是负载均衡，所有客户端都访问一个节点肯定会影响Redis工作效率，有了主从以后，查询操作就可以通过查询从节点来完成。
# 　　对主从模式必须的理解（结论已经验证过，可以自行验证）：
#
# 一个Master可以有多个Slaves
# 默认配置下，master节点可以进行读和写，slave节点只能进行读操作，写操作被禁止
# 不要修改配置让slave节点支持写操作，没有意义，原因一，写入的数据不会被同步到其他节点；原因二，当master节点修改同一条数据后，slave节点的数据会被覆盖掉
# slave节点挂了不影响其他slave节点的读和master节点的读和写，重新启动后会将数据从master节点同步过来
# master节点挂了以后，不影响slave节点的读，Redis将不再提供写服务，master节点启动后Redis将重新对外提供写服务。
# master节点挂了以后，不会slave节点重新选一个master
# 　　对有密码的情况说明一下，当master节点设置密码时：
#
# 客户端访问master需要密码
# 启动slave需要密码，在配置中进行配置即可
# 客户端访问slave不需要密码
# 2.1 主从节点的缺点
# 　　主从模式的缺点其实从上面的描述中可以得出：
#
# master节点挂了以后，redis就不能对外提供写服务了，因为剩下的slave不能成为master
# 　　这个缺点影响是很大的，尤其是对生产环境来说，是一刻都不能停止服务的，所以一般的生产坏境是不会单单只有主从模式的。所以有了下面的sentinel模式。
#
# 三、sentinel模式
# 　　sentinel模式的简介和配置，此处不再说，参照下面的博客：Redis Sentinel模式详解。
#
# 　　sentinel的中文含义是哨兵、守卫。也就是说既然主从模式中，当master节点挂了以后，slave节点不能主动选举一个master节点出来，那么我就安排一个或多个sentinel来做这件事，当sentinel发现master节点挂了以后，sentinel就会从slave中重新选举一个master。
#
# 　　对sentinel模式的理解：
#
# sentinel模式是建立在主从模式的基础上，如果只有一个Redis节点，sentinel就没有任何意义
# 当master节点挂了以后，sentinel会在slave中选择一个做为master，并修改它们的配置文件，其他slave的配置文件也会被修改，比如slaveof属性会指向新的master
# 当master节点重新启动后，它将不再是master而是做为slave接收新的master节点的同步数据
# sentinel因为也是一个进程有挂掉的可能，所以sentinel也会启动多个形成一个sentinel集群
# 当主从模式配置密码时，sentinel也会同步将配置信息修改到配置文件中，不许要担心。
# 一个sentinel或sentinel集群可以管理多个主从Redis。
# sentinel最好不要和Redis部署在同一台机器，不然Redis的服务器挂了以后，sentinel也挂了
# sentinel监控的Redis集群都会定义一个master名字，这个名字代表Redis集群的master Redis。
#  　　当使用sentinel模式的时候，客户端就不要直接连接Redis，而是连接sentinel的ip和port，由sentinel来提供具体的可提供服务的Redis实现，这样当master节点挂掉以后，sentinel就会感知并将新的master节点提供给使用者。
#
# 　　sentinel模式基本可以满足一般生产的需求，具备高可用性。但是当数据量过大到一台服务器存放不下的情况时，主从模式或sentinel模式就不能满足需求了，这个时候需要对存储的数据进行分片，将数据存储到多个Redis实例中，就是下面要讲的。
#
# 四、cluster模式
# 　　sentinel模式的简介和配置，此处不再说，参照下面的博客：Redis cluster模式详解。
#
# 　　cluster的出现是为了解决单机Redis容量有限的问题，将Redis的数据根据一定的规则分配到多台机器。对cluster的一些理解：
#
# cluster可以说是sentinel和主从模式的结合体，通过cluster可以实现主从和master重选功能，所以如果配置两个副本三个分片的话，就需要六个Redis实例。
# 因为Redis的数据是根据一定规则分配到cluster的不同机器的，当数据量过大时，可以新增机器进行扩容
# 　　这种模式适合数据量巨大的缓存要求，当数据量不是很大使用sentinel即可。

###########################################################
# 1.确保 所有哨兵端口都开启

# 2.所有的节点端口开启

# 3.配置文件 bind 不能为127.0.0.1 应该是 0.0.0.0
from redis.sentinel import Sentinel

# 连接哨兵服务器(主机名也可以用域名)
sentinel = Sentinel([('192.168.56.101', 26379)], socket_timeout=0.5)



# 获取主服务器地址
master = sentinel.discover_master('mymaster')
print(master)
# 输出：('172.31.0.2', 5001)


# 获取从服务器地址
slave = sentinel.discover_slaves('mymaster')
print(slave)
# 输出：[('172.31.3', 5001), ('172.31.0.4', 5001), ('172.31.0.5', 5001)]



# 获取主服务器进行写入
master = sentinel.master_for('mymaster', socket_timeout=0.5, db=15)
w_ret = master.set('foo', 'bar')
# 输出：True


# # 获取从服务器进行读取（默认是round-roubin）
slave = sentinel.slave_for('mymaster', socket_timeout=0.5, db=15)
r_ret = slave.get('foo')
print(r_ret)
# # 输出：bar