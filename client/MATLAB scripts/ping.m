function returnVal = ping(host,port)
    t = tcpip(host, port, 'NetworkRole', 'client');
    fopen(t)
    fwrite(t, data)
end

