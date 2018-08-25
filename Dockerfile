FROM centos:7

ENV PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
ENV JAVA_HOME /usr/lib/jvm/java-1.8.0-openjdk


RUN yum update -y \
        &&  yum install -y wget \
        java-1.8.0-openjdk-devel -y \
        git

RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py \
&& python get-pip.py

#RUN pip install flask \
#&& pip install flask_httpauth

COPY requirements.txt /

RUN pip install -r requirements.txt

EXPOSE 80

CMD python /codigo_aplicacao/app/app.py