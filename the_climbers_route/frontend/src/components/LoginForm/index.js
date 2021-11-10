import React from "react";

const LoginForm = ({ username, setUsername, password, setPassword, onSubmit }) => {
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
                type="password"
                value={password}
                onChange={e => setPassword(e.target.value)}
                title="password"
                minlength="8"
                required
            />
            <button onClick={onSubmit}>Login</button>
        </div>
    )
}

export default LoginForm;