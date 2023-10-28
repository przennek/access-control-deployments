<template>
  <div class="container">
    <img ref="video" class="video" src="../assets/standby.png">
    <audio id="audio" ref="audio" src="" type="audio/x-wav;codec=pcm" class="hidden" preload="none"></audio>
    <button @click="toggleAudioStream">{{ streaming ? 'Stop Streaming' : 'Start Streaming' }}</button>
  </div>
</template>

<script setup>
    import { ref, onMounted, onBeforeUnmount } from 'vue';
    import { useRouter } from 'vue-router';
    import { redirectToStandbyOnEndedCall } from '../api/api.js';
    import socket from '../api/socket.js';

    const audio = ref(null);
    const streamingAudio = ref(null);
    const video = ref(null);
    const streaming = ref(false);
    const router = useRouter();
    let pollTimer;
    const pollInterval = 500;

    const toggleAudioStream = () => {
      // Connect to the Socket.IO server when starting audio streaming
      socket.connect();
      captureMicrophoneData();
    };

    const captureMicrophoneData = () => {
      navigator.mediaDevices
        .getUserMedia({ audio: true })
        .then((stream) => {
          const audioContext = new AudioContext();
          const audioSource = audioContext.createMediaStreamSource(stream);

          const analyser = audioContext.createAnalyser();
          audioSource.connect(analyser);
          analyser.fftSize = 256;
          const bufferLength = analyser.frequencyBinCount;
          const dataArray = new Uint8Array(bufferLength);

          const getAudioDataAndSend = () => {
            analyser.getByteFrequencyData(dataArray);

            const dataToSend = JSON.stringify(Array.from(dataArray));
            socket.emit('audio_sink', dataToSend); // Use 'emit' to send data
            requestAnimationFrame(getAudioDataAndSend);
          };

          getAudioDataAndSend();
        })
        .catch((error) => {
          console.error('Error accessing microphone:', error);
        });
    };

    onMounted(() => {
      pollTimer = setInterval(async () => redirectToStandbyOnEndedCall(router, video), pollInterval);
      video.value.setAttribute("src", "https://bramka/api/stream/video_feed")
      audio.value.setAttribute("src", "https://bramka/api/stream/audio_feed")
      audio.value.play();
    });

    onBeforeUnmount(() => {
      clearInterval(pollTimer);
      video.value.setAttribute("src", "../assets/standby.png")
      audio.value.setAttribute("src", "")
      audio.value.pause();
    });
</script>

<style scoped>
    .container {
      width: 640px;
      height: 480px;
    }

    .video {
      width: 640px;
      height: 480px;
    }

    .hidden {
      display: none;
    }
</style>
