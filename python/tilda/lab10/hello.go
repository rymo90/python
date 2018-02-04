package main

import "fmt"

func main() {
	fmt.Println("Hello World")
	i := 2
	fmt.Print("write ", i, " as ")
	switch i {
	case 1:
		fmt.Println("one")
	case 2:
		fmt.Println("Two")
	}
	// fmt.Println(i)
}
