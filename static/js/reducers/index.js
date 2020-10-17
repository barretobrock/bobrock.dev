import { ADD_ARTICLE } from '../constants/action-types';

const initialState = {
    articles: []
};

function rootReducer(state = initialState, action) {
    if (action.type === ADD_ARTICLE) {
        // Push new article to store, but we'll have to concat, as `push`ing
        //  wouldn't keep the original state unaltered and thus would go
        //  against the Redux principle of immutibility. Thus, we use `concat` instead.
        return Object.assign({}, state, {
            articles: state.articles.concat(action.payload)
        })
    }
    return state;
}

export default rootReducer;