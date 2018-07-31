import Vue from 'vue'
import HelloWorld from './components/HelloWorld.vue'

Vue.config.productionTip = false

Vue.component('hello', HelloWorld)

new Vue({el: '#app'})

