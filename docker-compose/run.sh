docker rm -f myapp
docker rm -f mydb
docker build -t myapp app
docker build -t mydb db
docker run -e DBPORT=3000 -p3000:3000 -d --name mydb mydb
docker run -e DBPORT=3000 -e DBHOST=mydb -e MYPORT=5000 -p5000:5000 -d --name myapp --link mydb myapp

sleep 5
docker logs mydb
docker logs myapp

echo 'checking IP of mydb'
docker inspect mydb | grep IPAdd
echo 'checking IP of myapp'
docker inspect myapp | grep IPAdd


#docker link will add IP address of mydb container into /etc/hosts of myapp container.
#docker exec -it myapp cat /etc/hosts  | grep mydb



