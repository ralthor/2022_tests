package main

import (
	"fmt"
)

type UserData struct {
	firstName       string
	lastName        string
	email           string
	numberOfTickets uint
}

func main() {
	var conferenceName = "Go conference"
	var ticketNumber = 3
	var names [50]string

	numbers := testMethod()

	fmt.Printf("Welcome to the %v\n", conferenceName)
	fmt.Println("Enter your ticket number:")
	// fmt.Scan(&ticketNumber)
	fmt.Printf("Your ticket number is %v\n", ticketNumber)
	// fmt.Scan(&names[0])
	// fmt.Scan(&names[1])
	fmt.Printf("Names are %v\n", names)

	count := 6
	for count > 0 {
		numbers = append(numbers, count)
		count--
	}
	numbers = append(numbers, 12)
	numbers = append(numbers, 28)
	numbers = append(numbers, 3)

	// fmt.Println(numbers)
	// for index, number := range numbers {
	// 	fmt.Println(index, number)
	// }

	var n uint64 = 146

	var a uint64 = 1
	var b uint64 = 1
	var i uint64
	for i = 3; i <= n; i++ {
		c := a + b
		b = a
		a = c
	}
	fmt.Printf("The fib(%v) is %v\n", n, a)

	m := createMap()
	fmt.Println(m["test."])

	userList := dummyUserDataList()
	fmt.Println(userList)

	fmt.Println("done.")
}

func fib(n uint64) uint64 {
	if n <= 2 {
		return 1
	}
	return fib(n-1) + fib(n-2)
}

func testMethod() []int {
	var numbers []int
	numbers = append(numbers, 10)
	return numbers
}

func createMap() map[string]string {
	var myMap = map[string]string{}
	myMap["test"] = "test value!"
	return myMap
}

func dummyUserDataList() []UserData {
	list := createUserDataList()
	u := UserData{
		email:     "a@a.com",
		firstName: "Amin",
		lastName:  "AR",
	}
	list = append(list, u)
	return list
}

func createUserDataList() []UserData {
	return make([]UserData, 0)
}
