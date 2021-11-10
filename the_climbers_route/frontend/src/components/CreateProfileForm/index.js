// CREATE PROFILE FORM COMPONENT:
import React from "react";

const CreateProfileForm = ({ username, setUsername, first_name, setFirst_Name, last_name, setLast_Name, email, setEmail, password, setPassword, onSubmit }) => {
    return (
        <div>
            <input
                type="text"
                value={username}
                onChange={e => setUsername(e.target.value)}
                title="username"
                placeholder="username"
            />
            <input
                type="text"
                value={first_name}
                onChange={e => setFirst_Name(e.target.value)}
                title="first_name"
                placeholder="First Name"
            />
            <input
                type="text"
                value={last_name}
                onChange={e => setLast_Name(e.target.value)}
                title="last_name"
                placeholder="Last Name"
            />
            <input
                type="email"
                value={email}
                onChange={e => setEmail(e.target.value)}
                title="email"
                placeholder="Email"
            />
            <input
                type="password"
                value={password}
                onChange={e => setPassword(e.target.value)}
                title="password"
                minlength="8"
                required
            />
            <button onClick={onSubmit}>Create Account</button>
        </div>
    )
}

export default CreateProfileForm;