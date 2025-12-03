# Cache-Proxy Server
A proxy server that checks cache for requests; returns HIT if cached, otherwise forwards to the original server and caches the response
I used Cache Dic in Python we can use Redis for caching that is useful in big projects 

# 🧩 What Problem Does It Solve?

Instead of sending user requests directly to the main (origin) server, the system routes them through a proxy server. The proxy server checks whether the requested data already exists in its cache.

If the data is cached, the proxy server immediately returns it to the user, reducing load on the main server and improving response time.

If the data is not cached, the proxy server forwards the request to the main server, retrieves the data, stores it in the cache, and then sends it back to the user.

This process improves performance, efficiency, and scalability while decreasing server load and latency.

# How to install

pip install -r requirments.txt

# activate the venv
.\proxy_venv\Scripts\Activate.ps1


# how to run FastAPI proxy server
python main.py --proxy 3000

# Project URL

http://127.0.0.1:3000/docs#/
