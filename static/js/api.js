import React, { Component } from 'react';

export default class API extends Component {
    constructor() {
        super();
        this.state = {
            resp: []
        }
    }

    fetchAllPosts() {
        console.log('Fetching all tables...')
        fetch('/api/tbl/posts', {
            method: 'GET',
            mode: "no-cors",
            dataType: 'json'
        })
            .then(r => r.json())
            .then(r => {
                console.log(r)
                this.setState({
                    resp: r
                })
            })
            .catch(err => console.log(err))
    }

    render() {
        return (
            <div>
                <h3>Response:</h3>
                <p>
                    {this.state.resp.map()}
                </p>
                <button onClick={() => this.fetchAllPosts()}>Get all posts.</button>
            </div>
        );
    }
}





// const BASE_URI = 'http://localhost:4433';


// const client = axios.create({
//  baseURL: BASE_URI,
//  json: true
// });
//
// class APIClient {
//  constructor() {
//
//  }
//
//
//  // createKudo(repo) {
//  //   return this.perform('post', '/kudos', repo);
//  // }
//  //
//  // deleteKudo(repo) {
//  //   return this.perform('delete', `/kudos/${repo.id}`);
//  // }
//
//  getFullPostsTable() {
//    return this.perform('get', '/kudos');
//  }
//
//  async perform (method, resource, data) {
//    return client({
//      method,
//      url: resource,
//      data,
//      headers: {}
//    }).then(resp => {
//      return resp.data ? resp.data : [];
//    })
//  }
// }
//
// export default APIClient;