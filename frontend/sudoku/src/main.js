import Vue from 'vue';
import BootstrapVue from 'bootstrap-vue';
import App from './App.vue';
import VueResource from 'vue-resource';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

// app.js
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';

Vue.config.productionTip = false;
Vue.use(BootstrapVue);
Vue.use(VueResource);
Vue.use(ElementUI);
Vue.http.options.root = '/root';
Vue.http.headers.common.Authorization = 'Basic YXBpOnBhc3N3b3Jk';

new Vue({
  render: h => h(App),
}).$mount('#app');
