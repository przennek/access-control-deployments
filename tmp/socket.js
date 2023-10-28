import io from 'socket.io-client';

// Connect to the Socket.IO server
const socket = io('https://bramka:443', {
  transports: ['websocket'], // Use WebSocket transport
  autoConnect: false, // Disable auto-connect to allow manual control
});

// Handle socket connection event
socket.on('connect', () => {
  console.log('Connected to Socket.IO server');
});

// Handle socket disconnection event
socket.on('disconnect', () => {
  console.log('Disconnected from Socket.IO server');
});

export default socket;