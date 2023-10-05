import MediaRecorderService from "./MediaRecorderService";

const isAudioEnabled = navigator.mediaDevices.getUserMedia? true:false;

export default (audio, recordFile) => {

    let mediaRecorder;
    let chunks = [];

    const handleAudioUrl = (blob) => {

          const url = window.URL.createObjectURL(blob);
          audio.controls = true;
          audio.src = url;
    };
    const handleRecordFile = (files) => {
          recordFile.files = files;
    };

    const mrs = new MediaRecorderService(
        handleAudioUrl, handleRecordFile
    );

    const onStop = () =>{
        mrs.stop();
    }

    const onStart = () => {
        mrs.start();
    }

    return {
        onStop: onStop,
        onStart: onStart,
    };

};
