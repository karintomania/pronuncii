const isAudioEnabled = navigator.mediaDevices.getUserMedia? true:false;

export const assessmentInit = () => {

    function mediaRecorderClosure(){
        let mediaRecorder;
        let chunks = [];
        let audio;
        let recordFile;

        function init(stream){
            mediaRecorder = new MediaRecorder(stream);

            mediaRecorder.onstop = function(e){

              audio.controls = true;
              const blob = new Blob(chunks, { 'type' : 'audio/ogg; codecs=opus' });
              chunks = [];
              const audioURL = window.URL.createObjectURL(blob);
              audio.src = audioURL;

              let container = new DataTransfer();
              let file = new File([blob], "sound.wav",{type:"audio/wav"});
              container.items.add(file);
              recordFile.files = container.files;

            }

            mediaRecorder.ondataavailable = function(e) {
              chunks.push(e.data);
            }
        }

        function onStop(){
            audio = document.getElementById("audioClip");
            mediaRecorder.stop();
        }

        function onStart(audioElm, fileElm){
            audio = audioElm;
            recordFile = fileElm;
            mediaRecorder.start();
        }

        return {
            init: init,
            onStop: onStop,
            onStart: onStart,
        };

    }

    const {init, onStop, onStart} = mediaRecorderClosure();

    function onError(err) {
     console.log('The following error occured: ' + err);
    }

  navigator.mediaDevices
        .getUserMedia({ audio: true })
        .then(init, onError);

    return {
        onStart: onStart,
        onStop: onStop,
    };
};

export default assessmentInit;
