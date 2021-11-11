import React, {useEffect, useState} from "react";
import CreateProfileForm from "../../components/CreateProfileForm";
import LoginForm from "../../components/LoginForm";
import axiosInstance from "../../api/axiosApi";

const SplashPage = () => {
    const[username, setUsername] = useState("");
    const[first_name, setFirst_Name] = useState("");
    const[last_name, setLast_Name] = useState("");
    const[email, setEmail] = useState("");
    const[password, setPassword] = useState("");

    useEffect(() => {
        if (localStorage.getItem('access_token')) {
            console.log("you appear to be logged in")
        } else {
            console.log("You are not logged in")
        }
    }, []);

    const onSubmitLogin = async(e) => {
        e.preventDefault();
        try {
            axiosInstance.post('/token/obtain/', {
                'username': username,
                'password': password
            }).then(res => {
                axiosInstance.defaults.headers['Authorization'] = "JWT " + res.data.access;
                localStorage.setItem('access_token', res.data.access);
                localStorage.setItem('refresh_token', res.data.refresh);
                console.log("here's the data we got back", res.data);
                setUsername("");
                setPassword("");
            });
        } catch (error) {
            throw error;
        }
    }

    const onSubmitProfile = async () => {
        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                username,
                first_name,
                last_name,
                email,
                password,
            }),
        };
        fetch('/api/registration/signup', requestOptions)
        .then((res) => res.json())
        .then((data) => console.log("data has been received:", data));
    }

    return (
        <div>
            <div>
                Testing if the splash page is working.
            </div>
            <CreateProfileForm 
                username = {username}
                setUsername = {setUsername}
                first_name = {first_name}
                setFirst_Name = {setFirst_Name}
                last_name = {last_name}
                setLast_Name = {setLast_Name}
                email = {email}
                setEmail = {setEmail}
                password = {password}
                setPassword = {setPassword}
                onSubmit = {onSubmitProfile}
            />
            <LoginForm 
                username = {username}
                setUsername = {setUsername}
                password = {password}
                setPassword = {setPassword}
                onSubmit = {(e) => onSubmitLogin(e)}
            />
        </div>
    );
}

export default SplashPage;