package main

import (
	"errors"
	"flag"
	"fmt"
	"log"
	"net"
	"os"
	"time"

	"github.com/google/gopacket/pcap"
)

var (
	downStreamDataSize = 0
	upStreamDataSize   = 0
	deviceName         = flag.String("i", "eth0", "network interface device name")
)

func main() {

	flag.Parse()

	//Find All Devices
	devices, err := pcap.FindAllDevs()
	if err != nil {
		log.Fatal(err)
	}

	//Find Exact devices
	var device pcap.Interface
	for _, d := range devices {
		if d.Name == *deviceName {
			device = d
		}
	}

	//Obtain the mac address of the networl card according to ipv4
	macAddr, err := findMacAddrByIp(findDeviceIpv4(device))
	if err != nil {
		panic(err)
	}

	fmt.Printf("Chosen Device's IPv4: %s\n", findDeviceIpv4(device))
	fmt.Printf("Chosen Device Mac: %s\n", macAddr)

	go monitor()

}

//Obtain the mac address bind to IPv4 NIC. This method is used because gopacket does not encapsulate the method of obatining MAC address internally.
// Look for Mac address by getting the NIC
func findMacAddrByIp(ip string) (string, error) {
	interfaces, err := net.Interfaces()
	if err != nil {
		panic(interfaces)
	}

	for _, i := range interfaces {
		addrss, err := i.Addrs()
		if err != nil {
			panic(err)
		}

		for _, addr := range addrss {
			if a, ok := addr.(*net.IPNet); ok {
				if ip == a.IP.String() {
					return i.HardwareAddr.String(), nil
				}
			}
		}

	}
	return "", errors.New(fmt.Sprintf("No devices has given IP: %s", ip))
}

func findDeviceIpv4(device pcap.Interface) string {
	for _, addr := range device.Addresses {
		if ipv4 := addr.IP.To4(); ipv4 != nil {
			return ipv4.String()
		}
	}

	panic("Device has no ipv4")
}

func monitor() {
	for {

		os.Stdout.WriteString(fmt.Sprintf("\rDownload Speed : %.2fkb/s \t Upload Speed : %.2fkb/s", float32(downStreamDataSize)/1024/1, float32(upStreamDataSize)/1024/1))
		downStreamDataSize = 0
		upStreamDataSize = 0
		time.Sleep(1 * time.Second)
	}
}
