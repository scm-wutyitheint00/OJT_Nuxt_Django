export const state = () => ({
    posts: {}
})

export const mutations = ({
    ADD_POST(state, post) {
        state.posts = {title: post.title, description: post.description}
    }
})

export const getters = {
    getPost(state) {
      return state.posts
    }
  }