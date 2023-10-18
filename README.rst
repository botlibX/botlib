NAME

::

   LIBBOT - the python3 bot namespace


DESCRIPTION


::

    LIBBOT is a python3 library intended to be programmable  in a
    static, only code, no popen, no user imports and no reading
    modules from a directory, way. 

    LIBBOT provides a demo bot, it can connect to IRC, fetch and
    display RSS feeds, take todo notes, keep a shopping list
    and log text. You can also copy/past the service file and run
    it under systemd for 24/7 presence in a IRC channel.


SYNOPSIS


::

    bot <cmd> [key=val] 
    bot <cmd> [key==val]
    bot [-c] [-d] [-v] [-i]


INSTALL


::

    $ pipx install libbot


USAGE

::

    default action is doing nothing

    $ bot
    $

    first argument is a command

    $ bot cmd
    cfg,cmd,dlt,dne,dpl,fnd,log,met,mod,mre,
    nme,pwd,rem,rss,skl,sts,tdo,thr,udp,ver

    starting a console requires an option

    $ bot -c
    >

    list of modules

    $ bot mod
    bsc,err,flt,irc,log,mod,rss,shp,
    sts,tdo,thr,udp

    start as daemon

    $ bot -d
    $ 

    add -v if you want to have verbose logging


CONFIGURATION


::

    irc

    $ bot cfg server=<server>
    $ bot cfg channel=<channel>
    $ bot cfg nick=<nick>

    default channel is #bot on localhost

    sasl

    $ bot pwd <nsvnick> <nspass>
    $ bot cfg password=<frompwd>

    rss

    $ bot rss <url>
    $ bot dpl <url> <item1,item2>
    $ bot rem <url>
    $ bot nme <url< <name>


COMMANDS


::

    cmd - commands
    cfg - irc configuration
    dlt - remove a user
    dpl - sets display items
    ftc - runs a fetching batch
    fnd - find objects 
    flt - instances registered
    log - log some text
    met - add a user
    mre - displays cached output
    nck - changes nick on irc
    pwd - sasl nickserv name/pass
    rem - removes a rss feed
    rss - add a feed
    slg - slogan
    thr - show the running threads


SYSTEMD

::

    replace "<user>" with the user running pipx


    [Unit]
    Description=the python3 bot namespace
    Requires=network.target
    After=network.target

    [Service]
    Type=simple
    User=<user>
    Group=<user>
    WorkingDirectory=/home/<user>/.bot
    ExecStart=/home/<user>/.local/pipx/venvs/libbot/bin/botd
    RemainAfterExit=yes

    [Install]
    WantedBy=multi-user.target


    default channel is #botd on localhost.


FILES

::

    ~/.bot
    ~/.local/bin/bot
    ~/.local/bin/botcmd
    ~/.local/bin/botd
    ~/.local/pipx/venvs/libbot/


AUTHOR

::

    botlib <botlib@proton.me>


COPYRIGHT

::

    LIBBOT is placed in the Public Domain.
