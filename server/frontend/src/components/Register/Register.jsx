import React, { useState } from "react";
import "./Register.css";

const Register = () => {
  const [userName, setUserName] = useState("");
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");

  const [loading, setLoading] = useState(false);
  const [errorMessage, setErrorMessage] = useState("");
  const [successMessage, setSuccessMessage] = useState("");

  const validateEmail = (val) => {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(val);
  };

  const handleRegister = async (e) => {
    e.preventDefault();
    setErrorMessage("");
    setSuccessMessage("");

    // Client-side validations
    if (!userName.trim()) {
      setErrorMessage("Username is required.");
      return;
    }
    if (!firstName.trim()) {
      setErrorMessage("First Name is required.");
      return;
    }
    if (!lastName.trim()) {
      setErrorMessage("Last Name is required.");
      return;
    }
    if (!email.trim()) {
      setErrorMessage("Email address is required.");
      return;
    }
    if (!validateEmail(email.trim())) {
      setErrorMessage("Please enter a valid email address.");
      return;
    }
    if (!password) {
      setErrorMessage("Password is required.");
      return;
    }
    if (password.length < 6) {
      setErrorMessage("Password must be at least 6 characters.");
      return;
    }
    if (confirmPassword && password !== confirmPassword) {
      setErrorMessage("Passwords do not match.");
      return;
    }

    setLoading(true);

    try {
      const registerUrl = "/register/";
      const response = await fetch(registerUrl, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          username: userName.trim(),
          first_name: firstName.trim(),
          last_name: lastName.trim(),
          email: email.trim(),
          password: password,
        }),
      });

      const data = await response.json();

      if (response.ok && (data.status || response.status === 201)) {
        setSuccessMessage("Registration successful! You can now log in.");
        setUserName("");
        setFirstName("");
        setLastName("");
        setEmail("");
        setPassword("");
        setConfirmPassword("");
      } else {
        setErrorMessage(data.error || data.message || "Registration failed. Please try again.");
      }
    } catch (err) {
      setErrorMessage("Network error: Could not reach registration server.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="register_container">
      <div className="register_card">
        <div className="register_header">
          <p className="register_eyebrow">CREATE AN ACCOUNT</p>
          <h2 className="register_title">Sign Up</h2>
          <p className="register_subtitle">
            Join our dealership portal to browse vehicles and share verified reviews.
          </p>
        </div>

        {errorMessage && (
          <div className="register_alert register_alert_error" role="alert" id="registerError">
            {errorMessage}
          </div>
        )}

        {successMessage && (
          <div className="register_alert register_alert_success" role="alert" id="registerSuccess">
            {successMessage}
          </div>
        )}

        <form onSubmit={handleRegister} className="register_form" noValidate>
          <div className="form_group">
            <label htmlFor="username">Username *</label>
            <input
              type="text"
              id="username"
              name="username"
              placeholder="Choose a username"
              value={userName}
              onChange={(e) => setUserName(e.target.value)}
              disabled={loading}
              required
            />
          </div>

          <div className="form_row">
            <div className="form_group">
              <label htmlFor="firstName">First Name *</label>
              <input
                type="text"
                id="firstName"
                name="firstName"
                placeholder="First name"
                value={firstName}
                onChange={(e) => setFirstName(e.target.value)}
                disabled={loading}
                required
              />
            </div>

            <div className="form_group">
              <label htmlFor="lastName">Last Name *</label>
              <input
                type="text"
                id="lastName"
                name="lastName"
                placeholder="Last name"
                value={lastName}
                onChange={(e) => setLastName(e.target.value)}
                disabled={loading}
                required
              />
            </div>
          </div>

          <div className="form_group">
            <label htmlFor="email">Email Address *</label>
            <input
              type="email"
              id="email"
              name="email"
              placeholder="you@example.com"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              disabled={loading}
              required
            />
          </div>

          <div className="form_row">
            <div className="form_group">
              <label htmlFor="password">Password *</label>
              <input
                type="password"
                id="password"
                name="password"
                placeholder="Enter password (min 6 characters)"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                disabled={loading}
                required
              />
            </div>

            <div className="form_group">
              <label htmlFor="confirmPassword">Confirm Password</label>
              <input
                type="password"
                id="confirmPassword"
                name="confirmPassword"
                placeholder="Re-enter password"
                value={confirmPassword}
                onChange={(e) => setConfirmPassword(e.target.value)}
                disabled={loading}
              />
            </div>
          </div>

          <button
            type="submit"
            className="register_submit_btn"
            id="registerButton"
            disabled={loading}
          >
            {loading ? "Registering..." : "Register"}
          </button>
        </form>

        <div className="register_footer">
          <p>
            Already have an account? <a href="/login/">Log in here</a>
          </p>
        </div>
      </div>
    </div>
  );
};

export default Register;
