import '@fortawesome/fontawesome-free/js/fontawesome.min'
import '@fortawesome/fontawesome-free/js/solid.min'

import Alpine from 'alpinejs';
window.Alpine = Alpine;

import assessment from './main/assessment';
Alpine.data('assessment', assessment);

Alpine.start();
