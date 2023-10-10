import '@fortawesome/fontawesome-free/js/fontawesome'
import '@fortawesome/fontawesome-free/js/solid'
import '@fortawesome/fontawesome-free/js/regular'
import '@fortawesome/fontawesome-free/js/brands'

import Alpine from 'alpinejs';
window.Alpine = Alpine;

import assessment from './main/assessment';
Alpine.data('assessment', assessment);

Alpine.start();
