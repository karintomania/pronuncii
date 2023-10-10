class MediaRecorderService{
    #mediaRecorder;
    chunks = [];

    constructor(handleAudioUrl, handleRecordFile){

        navigator.mediaDevices
            .getUserMedia({ audio: true })
            .then(
                (stream) => {
                    this.#init(stream, handleAudioUrl, handleRecordFile)
                }, this.#onError);

    }

    #init(stream, handleAudioUrl, handleRecordFile){
        this.#mediaRecorder = new MediaRecorder(stream);

        this.#setOndataavailable(handleAudioUrl, handleRecordFile);
        this.#setOnStop(handleAudioUrl, handleRecordFile);
    }

    #onError(err) {
        console.log('The following error occured: ' + err);
    }

    #setOndataavailable(){

        this.#mediaRecorder.ondataavailable = (e) => {
            this.chunks.push(e.data);
        }

    }

    #setOnStop(handleAudioUrl, handleRecordFile){

            this.#mediaRecorder.onstop = (e) => {

                // create blob
              const blob = new Blob(this.chunks, { 'type' : 'audio/ogg; codecs=opus' });
              this.chunks = [];

              // set audio URL
              handleAudioUrl(blob);

              // set file
              let container = new DataTransfer();
              let file = new File([blob], "sound.wav",{type:"audio/wav"});
              container.items.add(file);
              handleRecordFile(container.files);

            }

    }

    start(){
        this.#mediaRecorder.start();
    }

    stop(){
        this.#mediaRecorder.stop();
    }
}

export default MediaRecorderService;
