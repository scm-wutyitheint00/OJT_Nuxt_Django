export default function ({ store, redirect }) {
    if (process.client && !store.getters["isLoggedIn"]) return redirect("/login");
    // return redirect(404, '/el?e=rnf')
}

