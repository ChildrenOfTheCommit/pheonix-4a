import axios from 'axios'

const axiosInstance = axios.create({
	baseURL: import.meta.env.VITE_API_BASE_URL,
	timeout: 60000,
	headers: {
		'Content-Type': 'application/json'
	}
})

axiosInstance.interceptors.request.use((config) => {
	const accessToken = localStorage.getItem('access_token')

	if (accessToken) {
		config.headers.Authorization = `Bearer ${accessToken}`
	}
	return config
})

export default axiosInstance
