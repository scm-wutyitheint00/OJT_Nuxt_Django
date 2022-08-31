export const state = () => ({
  posts: {},
  user: {},
  loginData: {},
  isMember: false
})

export const mutations = ({
  ADD_POST(state, post) {
    state.posts = { title: post.title, description: post.description }
  },
  ADD_USER(state, user) {
    state.user = {
      name: user.name,
      email: user.email,
      password: user.password,
      confirmPassword: user.confirmPassword,
      type: user.type,
      phone: user.phone,
      dob: user.dob,
      address: user.address,
      profile: user.profile
    }
  },
  ADD_LOGIN_DATA(state, datas) {
    state.loginData = datas;
  }, 
  SET_MEMBER(state, data) {
    state.isMember = data;
      this.$router.push('/post');
  }
})

export const getters = {
  getPost(state) {
    return state.posts
  },
  getUser(state) {
    return state.user
  },
  isAuthenticated(state) {
    return state.auth.loggedIn
  },
  loggedInUser(state) {
    return state.auth.user
  },
  getLoginData(state) {
    return state.loginData
  }
}