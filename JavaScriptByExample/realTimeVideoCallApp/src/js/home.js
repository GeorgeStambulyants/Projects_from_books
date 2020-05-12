import './general';
import SimpleWebRTC from 'simplewebrtc';


const webrtc = new SimpleWebRTC({
    localVideoEl: 'localVideo',
    remoteVideoEl: '',
    autoRequestMedia: true,
    debug: true,
});

class Home {
    constructor() {
        this.roomName = '';

        this.$createRoomSection = document.querySelector('#createRoomSection');
        this.$createRoomButton = document.querySelector('#createRoom');
        this.$roomNameInput = document.querySelector('#roomNameinput');

        this.$infoSection = document.querySelector('#infoSection');
        this.$roomName = document.querySelector('#roomNameText');
        this.$roomUrl = document.querySelector('#roomUrl');
        this.$buttonArea = document.querySelector('.room-text');
        this.$copy = document.querySelector('.copy');
        this.$copied = document.querySelector('.copied');

        this.$remotes = document.querySelector('video-area');
        this.$localVideo = document.querySelector('#localVideo');
    }
}


const home = new Home();