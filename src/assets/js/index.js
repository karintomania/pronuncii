import Alpine from 'alpinejs'

window.Alpine = Alpine
 
Alpine.start()

function mainInit(){
    return {
        testVar: "aaaa"
    }
};
 
window.mainInit = mainInit
