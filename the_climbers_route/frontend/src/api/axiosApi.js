import axios from 'axios';

// This allows our API to work while we're in development.

let HOST;
if (process.env.NODE_ENV !== "production") {
    HOST = "http://localhost:5000/api";
}
else {
    HOST ="https://project3-app-flex525.herokuapp.com/api"
}


// Creates an instance of axios.
export default axios.create({
    baseURL: HOST,
    timeout: 5000,
    headers: {
        'Authorization': "JWT " + localStorage.getItem('access_token'),
        'Content-Type': 'application/json',
        'accept': 'application/json'
    }
});