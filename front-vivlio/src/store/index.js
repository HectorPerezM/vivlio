import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import signUp from '@/store/signUp.js'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    books: []
  },
  mutations: {
    books (state, data) {
      state.books = data
    }
  },
  actions: {
    getBook: async function ({ commit, state }, title) {
      console.log("GET BOOK STORE!");
      const params = '*' + title + '*'
      let data = []
      await axios.get(`http://0.0.0.0:8000/api/books/?title__wildcard=${params}`)
        .then(response => (data = response.data)).catch(error => { console.log(error) })
      console.log(data);

      commit('books', data)
    }
  },
  modules: {
    signUp
  }
})
