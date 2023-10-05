import Alpine from 'alpinejs';
window.Alpine = Alpine;

import assessment from './main/assessment';
Alpine.data('assessment', assessment);

Alpine.start();
