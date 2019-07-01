# ChronoSync
Program for time synchronization on ChronoTrack devices.

The program is used when it is necessary to synchronize the device on the race route (split points, very rarely on start/meta point).
Time synchronization is implemented by sending a message via UDP with the current computer time. 

example message: CTCTime:F:2019.07.01-21:56:25.54:Manual

Program use standard socket module.

Due to delays when sending messages, it is not recommended to use on national championnschip etc.
The delay when using the internal network is negligible, but for example using own vpn server on Qnap it can reach up to two seconds. 

UDP PORT: 10006 - default for ChronoTrack device
