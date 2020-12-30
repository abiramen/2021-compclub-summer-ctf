# CompClub Summer CTF 2021

This repo contains the challenges used in the 2021 CSESoc CompClub CTF, which was targeted at high school students in teams of 3-4, running . as well as accompanying writeups, and source files.

In case future co-ordinators of CompClub CTFs are unsure as to how the infrastructure was set up, the following guide is just for you!

## Infrastructure

We chose to use [CTFd](https://github.com/ctfd/ctfd) as our platform for the CTF, mostly due to my familiarity using it both as a competitor (CTFd is quite commonly used), and helping run CTFs with SecSoc.

After weighing up several options, we hosted CTFd on a DigitalOcean Droplet (just a VM), and containers for other challenges on another smaller droplet. This cost us nothing thanks to $100 of DigitalOcean credits - it would've normally cost {insert amount here} (this includes running lightweight droplets 2 weeks ahead of the CTF, scaling up the CTFd droplet for 4 hours of the CTF, and keeping the challenges up for 10 days after.). A Google search should yield you a promo code/referral link to achieve the same, or you can opt to use another cloud infra service.

The following will step you through getting CTFd up and running.

1. Create a DigitalOcean droplet (or whatever service you're using).
    - I would recommend setting the server location in San Francisco - as of the time of writing, it has a ping of ~240ms (which seems high, but is OK for hosting CTFd).
    - While setting up the CTF, you can choose the smallest droplet size (1 vCPU, 1GB RAM, 25GB disk).
    - Install Ubuntu on it.
    - I would recommend adding an SSH key for easy access.
    - If you know how to use `docker-machine`, you can probably figure out how to do Steps 1-4 from there.
2. SSH, or get a shell into the droplet once it is set up.
    - You can exclude the `sudo` in future commands if you're logged in as root.
3. Follow the instructions to install Docker on your Droplet [here](https://docs.docker.com/engine/install/).
4. We want to now create a container from the CTFd image.
    - `docker run -d -p 8000:8000 ctfd/ctfd:latest --restart unless-stopped`
5. We now need a domain to point to our CTF. CSESoc probably has spare domains. In our case, I registered `compclub.xyz`. Access the DNS settings with your domain registrar, and set up an `A` record to point to the IP of your DigitalOcean droplet. 
6. Once the DNS record has been updated (this may take some time to propagate), we can now set up a firewall, rate limiting and SSL. Before we can do this, we will need to stop the container. To get the container ID, use `docker container ls`. Use this ID to stop the container with `docker container stop your-container-id`.
7. Install nginx and ufw.
    - Make sure that your packages are up to date with `sudo apt update`.
    - Install with `sudo apt install nginx ufw`.
8. Run the following commands to allow HTTP(s) and ssh through
    - `sudo ufw allow 'Nginx Full' && sudo ufw allow 'OpenSSH'`
9. Enable the firewall.
    - `sudo ufw enable`
10. To configure Nginx to route requests to CTFd, create a file (using your preferred terminal text editor such as vi or nano) at `etc/nginx/sites-available/yourdomain.com`, replacing with the name of your domain. Insert the following contents, making sure to replace with your own domain on the 4th line.
```
limit_req_zone  $binary_remote_addr zone=mylimit:10m rate=10r/s;
limit_conn_zone $binary_remote_addr zone=addr:10m;
server {
	server_name yourdomain.com;
	limit_req zone=mylimit burst=15;
	limit_conn addr 10;
	limit_req_status 429;
	client_max_body_size 8M;
	location / {
    		proxy_pass http://localhost:8000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
  }
}
```
11. Use the following command to create a symlink, replacing domains (twice) again.
    - `sudo ln -s /etc/nginx/sites-available/yourdomain.com /etc/nginx/sites-enabled/yourdomain.com`
    - Reload nginx with `sudo nginx -s reload`.
12. We need to now generate an SSL certificate so that we can allow for, and enforce HTTPS connections for CTFd.
    - Install certbot, a tool to generate free SSL certs with `sudo apt install certbot`.
13. Run `sudo certbot --nginx` and follow the steps ahead.
14. Restart your Docker container with `docker container start your-container-id`

Yay! You should now have a running CTFd instance and should be able to connect over HTTPS with your domain! Make sure to visit the page to set up your admin CTFd account.

You can scale up your droplet a few hours before your CTF so that you have more vCPUs and RAM to run the CTF. We used {insert droplet config here}.

-- still a work in progress --

### Credits
I based this guide off my experience setting up, which was mostly thanks to:
- https://www.coengoedegebure.com/hosting-a-ctf-made-easy/
- https://medium.com/csictf/self-hosting-a-ctf-platform-ctfd-90f3f1611587
- https://github.com/lecafard
