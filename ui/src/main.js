import Vue from 'vue'

import './vuepress/styles/theme.styl'
import './sphinx-theme.styl'
import OutboundLink from './OutboundLink.vue'
import Navbar from './Navbar.vue'
import NavLinks from './NavLinks.vue'
import Sidebar from './Sidebar.vue'
import Page from './Page.vue'


Vue.config.productionTip = false

Vue.component('outboundlink', OutboundLink)
Vue.component('navbar', Navbar)
Vue.component('navlinks', NavLinks)
Vue.component('sidebar', Sidebar)
Vue.component('page', Page)


// fake router element
Vue.component('router-link', {
  props: ['to'],
  template: '<a :href="to"><slot></slot></a>',
})

new Vue({
  el: '#app',
  // taken from Layout.vue
  data: {
    isSidebarOpen: false,
    swUpdateEvent: null
  },
  computed: {
    pageClasses () {
      //const userPageClass = this.$page.frontmatter.pageClass
      return [
        {
         // 'no-navbar': !this.shouldShowNavbar,
          'sidebar-open': this.isSidebarOpen,
         // 'no-sidebar': !this.shouldShowSidebar
        },
       // userPageClass
      ]
    }
  },
  methods: {
    toggleSidebar (to) {
      this.isSidebarOpen = typeof to === 'boolean' ? to : !this.isSidebarOpen
    },
  },
})


