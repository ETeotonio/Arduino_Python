#define ethernet_h
#include <Ethernet.h>
#include <aREST.h>
 
aREST rest = aREST();
EthernetServer server(80);
void setLedStatus(String status);

 void setup() {
  Serial.begin(115200);
  Serial.println("Try DHCP...");
  rest.function("ledstatus",setLedStatus);
  server.begin();
  Serial.print("server IP: ");
  Serial.println(Ethernet.localIP());
  Serial.println("Setup complete.\n");
  pinMode(LED_BUILTIN,OUTPUT);
}

void loop() {
  // listen for incoming clients
  EthernetClient client = server.available();
  rest.handle(client);
}

void setLedStatus(String status){
  if(status == "On"){
    digitalWrite(LED_BUILTIN,HIGH);
  }else{
    digitalWrite(LED_BUILTIN,LOW);
  }
}
  
