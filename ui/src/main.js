import Vue from 'vue'

import './vuepress/styles/theme.styl'
import Navbar from './Navbar.vue'


Vue.config.productionTip = false

Vue.component('navbar', Navbar)

new Vue({el: '#app'})

