# csgo-covertchannel
This project is aimed at creating a covert communication channel between two users to asynchronously exchange messages. 
The code was written as a proof of concept for the original idea of creating a workshop map to encode data and hide it in plain sight as an "aim trainer" for the popular game Counter Strike:Global Offensive.

The project is currently incomplete as the actual implementation is still not ready but those .vmf and .bsp files should be up as soon as they are ready. 

For the POC implementation - change the file paths in the sender file. The "original" file can be any of the log files and the new encoded file has to have an extension of .txt. 

The main logic of the program is that if the player kills a bot on the <T> side that is a "0" and if the player kills a bot on the <CT> side that would considered a "1". A binary message can be encoded using this method. On the receiver end the user runs the receiver script to identify the order of <T> and <CT> bots. 
  
In theory, if the map has this method of encoding the receiver just has to download that workshop map (there's tons of people making workshop maps for aim training) and parse through the logs to decode the message. 
  
