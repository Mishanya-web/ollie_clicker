const gif2Duration = 930;

let isPlaying = false;

function isMobileDevice() {
    return ('ontouchstart' in window || navigator.maxTouchPoints > 0);
}

function setContainerDimensions() {
    const gifContainer = document.getElementById("gif-container");
    const screenHeight = window.innerHeight;
    const screenWidth = window.innerWidth;

    if (isMobileDevice()) {
        // Настройки для мобильных устройств
        gifContainer.style.height = `${screenHeight}px`;
        gifContainer.style.width = `${screenWidth}px`;
    } else {
        // Настройки для компьютеров
        gifContainer.style.height = `${screenHeight}px`;
        gifContainer.style.width = `${screenHeight / 2.2}px`;
    }
}

function changeGif() {
    const buttonGif = document.getElementById("button-gif");

    if (!isPlaying) {
        isPlaying = true;
        buttonGif.src = gif2;

        setTimeout(() => {
            buttonGif.src = gif1;
            isPlaying = false;
        }, gif2Duration);
    }
}

const gifButton = document.getElementById("gif-button");
gifButton.addEventListener('click', changeGif);
gifButton.addEventListener('touchstart', changeGif);

window.onload = setContainerDimensions;
window.onresize = setContainerDimensions;


const socket = new WebSocket('ws://' + window.location.host + '/ws/button/');
let sessionClicks = 0;

socket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    document.getElementById('counter').textContent = data.message;
};

function sendButtonPress() {
    if (socket.readyState === WebSocket.OPEN) {
        sessionClicks += 1;
        socket.send(JSON.stringify({
            'message': 'pressed'
        }));
    } else {
        console.error('WebSocket не открыт. Состояние:', socket.readyState);
    }
}

window.addEventListener('beforeunload', function(event) {

    if (socket.readyState === WebSocket.OPEN && sessionClicks > 0) {
        socket.send(JSON.stringify({
            'message': 'save'
        }));
    }
});