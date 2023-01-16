#include <iostream>
#include <winsock2.h>

int main()
{
    // Initialize Winsock
    WSADATA wsaData;
    int iResult = WSAStartup(MAKEWORD(2, 2), &wsaData);
    if (iResult != 0)
    {
        std::cout << "WSAStartup failed: " << iResult << std::endl;
        return 1;
    }

    // Create a socket
    SOCKET sock = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
    if (sock == INVALID_SOCKET)
    {
        std::cout << "Failed to create socket: " << WSAGetLastError() << std::endl;
        WSACleanup();
        return 1;
    }

    // Connect to the server
    sockaddr_in hint;
    hint.sin_family = AF_INET;
    hint.sin_port = htons(54000);
    hint.sin_addr.S_un.S_addr = inet_addr("127.0.0.1"); // use the IP address of the server
    if (connect(sock, (sockaddr *)&hint, sizeof(hint)) == SOCKET_ERROR)
    {
        std::cout << "Failed to connect to server: " << WSAGetLastError() << std::endl;
        closesocket(sock);
        WSACleanup();
        return 1;
    }

    // Send data to the server
    const char *sendData = "Hello from the client!";
    int bytesSent = send(sock, sendData, strlen(sendData), 0);
    if (bytesSent == SOCKET_ERROR)
    {
        std::cout << "Failed to send data: " << WSAGetLastError() << std::endl;
        closesocket(sock);
        WSACleanup();
        return 1;
    }

    // Receive data from the server
    char recvData[4096];
    int bytesReceived = recv(sock, recvData, 4096, 0);
    if (bytesReceived == SOCKET_ERROR)
    {
        std::cout << "Failed to receive data: " << WSAGetLastError() << std::endl;
        closesocket(sock);
        WSACleanup();
        return 1;
    }

    // Print the received data
    recvData[bytesReceived] = '\0'; // null-terminate the received data
    std::cout << "Received: " << recvData << std::endl;

    // Close the socket
    closesocket(sock);
    WSACleanup();

    return 0;
}
