import Vue from 'vue'

import './vuepress/styles/theme.styl'
import Navbar from './Navbar.vue'


Vue.config.productionTip = false

Vue.component('navbar', Navbar)

// fake router element
Vue.component('router-link', {
  props: ['to'],
  template: '<a :href="to"><slot></slot></a>',
})

new Vue({el: '#app'})


