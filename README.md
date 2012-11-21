#### Interceptor

Quick hack to intercept and log calls to any application. 
I've created this to understand which args and parameters are used by vagrant to call VirtualBox.

#### Testing

    $ ln -s interceptor.py ls
    $ python ls

#### Production

    include #/usr/bin/python at the beginning of interceptor.py
    chmod +x it
    change the config path to a safe location
    change log file to wherever you want
    move the original binary out of the way, configure it on interceptor_config.ini
    link interceptor.py to the original name
    check your log file
    profit

