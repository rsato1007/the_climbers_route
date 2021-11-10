import React, {useEffect, useState} from "react";
import CreateProfileForm from "../../components/CreateProfileForm";

const SplashPage = () => {
    const[username, setUsername] = useState("");
    const[first_name, setFirst_Name] = useState("");
    const[last_name, setLast_Name] = useState("");
    const[email, setEmail] = useState("");
    const[password, setPassword] = useState("");

    const onSubmit = async () => {
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
                onSubmit = {onSubmit}
            />
        </div>
    );
}

export default SplashPage;