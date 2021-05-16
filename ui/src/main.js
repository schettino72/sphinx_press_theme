import { createApp } from 'vue'
import App from './App.vue'

const app = createApp(App);


import './vuepress/styles/index.styl'
import './sphinx-theme.styl'
import OutboundLink from './components/OutboundLink.vue'
import Navbar from './components/Navbar.vue'
import NavLinks from './components/NavLinks.vue'
import Sidebar from './components/Sidebar.vue'
import Page from './components/Page.vue'


app.component('outboundlink', OutboundLink)
app.component('navbar', Navbar)
app.component('navlinks', NavLinks)
app.component('sidebar', Sidebar)
app.component('page', Page)


// fake router element
app.component('router-link', {
  props: ['to'],
  template: '<a :href="to"><slot></slot></a>',
})


// mount with isHydrate===true
app.mount('#app', true);
