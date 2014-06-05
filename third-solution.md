**Solution of 3rd Part**
========================

 - There are 2/3 small glitches (found so far) in the given configuration. First, we have to put a ``server`` section for specifying the serving connectivity and other. Secondly, placing the config ``multi_accept on`` outside the ``event`` section seems to be better.

 - The following modification can be made to achieve the desired goal

    <pre>
        <code>
            user www-data;
            worker_processes 8;
            pid /var/run/nginx.pid;
            multi_accept on;
            events {
                    worker_connections 4096;
            }
            http {
                    sendfile on;
                    tcp_nopush on;
                    tcp_nodelay on;
                    keepalive_timeout 30;
                    types_hash_max_size 2048;
                    ….
                    …
                    ….
            }
            server {
                listen 80;
                client_max_body_size 50M;
                root /data/ez/current/public;
                access_log  /var/log/nginx.vhost.access.log  main;
            }
        </code>
    </pre>


 - Yes, external system with a little bit of caching ability like **VARNISH** will be helpful for to achieve the goal. As the content of the site is quite static in nature - implementing and using **VARNISH** will be just great.