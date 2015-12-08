##dockerfile创建：


- <p>Dockfile是一种被Docker程序解释的脚本，Dockerfile由一条一条的指令组成，每条指令对应Linux下面的一条命令。</p>

####<p>Dockerfile的书写规则及指令使用方法:<p>

- Dockerfile的指令是忽略大小写的，一般使用大写，使用 # 作为注释，每一行只支持一条指令，每条指令可以携带多个参数。


- Dockerfile的指令根据作用可以分为两种，构建指令和设置指令。构建指令用于构建image，其指定的操作不会在运行image的容器上执行；设置指令用于设置image的属性，其指定的操作将在运行image的容器中执行。

###1）FROM（指定基础image）
构建指令，必须指定且需要在Dockerfile其他指令的前面。后续的指令都依赖于该指令指定的image。FROM指令指定的基础image可以是官方远程仓库中的，也可以位于本地仓库。
<pre><code style="color: #000000;">FROM image	#指定基础image为该image的最后修改的版本
FROM image:tag 	#指定基础image为该image的一个tag版本
</pre></code>
###2) MAINTAINER（用来指定镜像创建者信息）
<p>构建指令，用于将image的制作者相关的信息写入到image中。当我们对该image执行docker inspect命令时，输出中有相应的字段记录该信息。</p>
<pre><code style="color: #000000;">MAINTAINER [name] 
</pre></code>
###3）RUN（安装软件用）
<p>构建指令，RUN可以运行任何被基础image支持的命令。如基础image选择了ubuntu，那么软件管理部分只能使用ubuntu的命令。该指令有两种格式：</p>
<pre><code style="color: #000000;">RUN <command> (the command is run in a shell - `/bin/sh -c`)  
RUN ["executable", "param1", "param2" ... ]  (exec form) 
</pre></code>
###4）CMD（设置container启动时执行的操作）
<p>设置指令，用于container启动时指定的操作。该操作可以是执行自定义脚本，也可以是执行系统命令。该指令只能在文件中存在一次，如果有多个，则只执行最后一条。该指令有三种格式：</p>
<pre><code style="color: #000000;">CMD ["executable","param1","param2"] (like an exec, this is the preferred form)  
CMD command param1 param2 (as a shell)  
</pre></code>
当Dockerfile指定了ENTRYPOINT，那么使用下面的格式：
<pre><code style="color: #000000;">CMD ["param1","param2"] (as default parameters to ENTRYPOINT)  
</pre></code>
<p>ENTRYPOINT指定的是一个可执行的脚本或者程序的路径，该指定的脚本或者程序将会以param1和param2作为参数执行。所以如果CMD指令使用上面的形式，那么Dockerfile中必须要有配套的ENTRYPOINT。</p>
###5）ENTRYPOINT（设置container启动时执行的操作）
<p>设置指令，指定容器启动时执行的命令，可以多次设置，但是只有最后一个有效。</p>
<pre><code style="color: #000000;">ENTRYPOINT ["executable", "param1", "param2"] (like an exec, the preferred form)  
ENTRYPOINT command param1 param2 (as a shell) 
</pre></code>
该指令的使用分为两种情况，一种是独自使用，另一种和CMD指令配合使用。
当独自使用时，如果你还使用了CMD命令且CMD是一个完整的可执行的命令，那么CMD指令和ENTRYPOINT会互相覆盖只有最后一个CMD或者ENTRYPOINT有效。
<pre><code style="color: #000000;">CMD echo “Hello, World!”  
ENTRYPOINT ls -l  
</pre></code>
<p>另一种用法和CMD指令配合使用来指定ENTRYPOINT的默认参数，这时CMD指令不是一个完整的可执行命令，仅仅是参数部分；ENTRYPOINT指令只能使用JSON方式指定执行命令，而不能指定参数。</p>
<pre><code style="color: #000000;">FROM ubuntu  
CMD ["-l"]  
ENTRYPOINT ["/usr/bin/ls"]  
</pre></code>
###6）USER（设置container容器的用户）
<p>设置指令，设置启动容器的用户，默认是root用户。</p>
<pre><code style="color: #000000;">ENTRYPOINT ["zabbix"]   #指定运行的zabbix用户
USER daemon  
或者
ENTRYPOINT ["zabbix", "-u", "daemon"]   
</pre></code>
###7）EXPOSE（指定容器需要映射到宿主机器的端口）
<p>设置指令，该指令会将容器中的端口映射成宿主机器中的某个端口。当你需要访问容器的时候，可以不是用容器的IP地址而是使用宿主机器的IP地址和映射后的端口。要完成整个操作需要两个步骤，首先在Dockerfile使用EXPOSE设置需要映射的容器端口，然后在运行容器的时候指定-p选项加上EXPOSE设置的端口，这样EXPOSE设置的端口号会被随机映射成宿主机器中的一个端口号。也可以指定需要映射到宿主机器的那个端口，这时要确保宿主机器上的端口号没有被使用。EXPOSE指令可以一次设置多个端口号，相应的运行容器的时候，可以配套的多次使用-p选项。 </p>
<pre><code style="color: #000000;">EXPOSE port [<port>...]  
</pre></code>

<pre><code style="color: #000000;"># 映射一个端口  
EXPOSE port1
相应的运行容器使用的命令
docker run -p port1 image 

映射多个端口
EXPOSE port1 port2 port3  

相应的运行容器使用的命令
docker run -p port1 -p port2 -p port3 image

还可以指定需要映射到宿主机器上的某个端口号
docker run -p host_port1:port1 -p host_port2:port2 -p host_port3:port3 image 
</pre></code>
<p>端口映射是docker比较重要的一个功能，原因在于我们每次运行容器的时候容器的IP地址不能指定而是在桥接网卡的地址范围内随机生成的。宿主机器的IP地址是固定的，我们可以将容器的端口的映射到宿主机器上的一个端口，免去每次访问容器中的某个服务时都要查看容器的IP的地址。对于一个运行的容器，可以使用docker port加上容器中需要映射的端口和容器的ID来查看该端口号在宿主机器上的映射端口。</p>

###8）ENV（用于设置环境变量）
<p>构建指令，在image中设置一个环境变量。</p>
<pre><code style="color: #000000;">ENV [key] [value]
</pre></code>

<p>设置了后，后续的RUN命令都可以使用，container启动后，可以通过docker inspect查看这个环境变量，也可以通过在docker run --env key=value时设置或修改环境变量。</p>
###9）ADD（从src复制文件到container的dest路径）
<p>构建指令，所有拷贝到container中的文件和文件夹权限为0755，uid和gid为0；如果是一个目录，那么会将该目录下的所有文件添加到container中，不包括目录；如果文件是可识别的压缩格式，则docker会帮忙解压缩（注意压缩格式）；如果<src>是文件且<dest>中不使用斜杠结束，则会将<dest>视为文件，<src>的内容会写入<dest>；如果<src>是文件且<dest>中使用斜杠结束，则会<src>文件拷贝到<dest>目录下。</p>
<pre><code style="color: #000000;">ADD [src] [dest]
</pre></code>
src:是相对被构建的源目录的相对路径，可以是文件或目录的路径，也可以是一个远程的文件url;
dest:是container中的绝对路径

###10）VOLUME（指定挂载点)
<p>设置指令，使容器中的一个目录具有持久化存储数据的功能，该目录可以被容器本身使用，也可以共享给其他容器使用。我们知道容器使用的是AUFS，这种文件系统不能持久化数据，当容器关闭后，所有的更改都会丢失。当容器中的应用有持久化数据的需求时可以在Dockerfile中使用该指令。</p>

<pre><code style="color: #000000;">VOLUME ["[mountpoint]"] 
</pre></code>

<pre><code style="color: #000000;">FROM base
VOLUME ["/tmp/data"]   
</pre></code>
<p>运行通过该Dockerfile生成image的容器，/tmp/data目录中的数据在容器关闭后，里面的数据还存在。例如另一个容器也有持久化数据的需求，且想使用上面容器共享的/tmp/data目录，那么可以运行下面的命令启动一个容器：</p>

<pre><code style="color: #000000;">docker run -t -i -rm -volumes-from container1 image2 bash  
</pre></code>
<p>container1为第一个容器的ID，image2为第二个容器运行image的名字。</p>
###11）WORKDIR（切换目录）
<p>设置指令，可以多次切换(相当于cd命令)，对RUN,CMD,ENTRYPOINT生效。</p>
<pre><code style="color: #000000;">WORKDIR /path/to/workdir 
</pre></code>

<pre><code style="color: #000000;"># 在 /p1/p2 下执行 vim a.txt 
WORKDIR /p1 WORKDIR p2 RUN vim a.txt  
</pre></code>

###12）ONBUILD（在子镜像中执行）

<pre><code style="color: #000000;">ONBUILD [Dockerfile关键字]
</pre></code>
<p>ONBUILD 指定的命令在构建镜像时并不执行，而是在它的子镜像中执行。</p>
