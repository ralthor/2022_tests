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

    // Bind the socket to an IP address and port
    sockaddr_in hint;
    hint.sin_family = AF_INET;
    hint.sin_port = htons(54000);
    hint.sin_addr.S_un.S_addr = INADDR_ANY;
    if (bind(sock, (sockaddr *)&hint, sizeof(hint)) == SOCKET_ERROR)
    {
        std::cout << "Failed to bind socket: " << WSAGetLastError() << std::endl;
        closesocket(sock);
        WSACleanup();
        return 1;
    }

    // Tell Winsock the socket is for listening
    if (listen(sock, SOMAXCONN) == SOCKET_ERROR)
    {
        std::cout << "Failed to listen on socket: " << WSAGetLastError() << std::endl;
        closesocket(sock);
        WSACleanup();
        return 1;
    }

    // Wait for a connection
    SOCKET client = accept(sock, nullptr, nullptr);
    if (client == INVALID_SOCKET)
    {
        std::cout << "Failed to accept client: " << WSAGetLastError() << std::endl;
        closesocket(sock);
        WSACleanup();
        return 1;
    }

    // Close the listening socket
    closesocket(sock);

    // Do some communication with the client
    char buf[4096];
    int bytesReceived = recv(client, buf, 4096, 0);
    if (bytesReceived == SOCKET_ERROR)
    {
        std::cout << "Failed to receive data from client: " << WSAGetLastError() << std::endl;
        closesocket(client);
        WSACleanup();
        return 1;
    }
    std::cout << "Received: " << std::string(buf, 0, bytesReceived) << std::endl;
    // Echo the data back to the client
    int bytesSent = send(client, buf, bytesReceived, 0);
    if (bytesSent == SOCKET_ERROR)
    {
        std::cout << "Failed to send data to client: " << WSAGetLastError() << std::endl;
        closesocket(client);
        WSACleanup();
        return 1;
    }
}