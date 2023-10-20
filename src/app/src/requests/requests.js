import axios from "axios";

const axios_instance = axios.create({
	baseURL: "http://localhost:8000/",
	withCredentials: false,
});

export const fetchData = async () => {
	const url = "";
	const body = null;
	try {
		const res = await axios_instance.get(url, body);
		return res.data ? res.data : null;
	} catch (err) {
		return { data: null, error: err.message ? err.message : "Not connected to the server" };
	}
};

export const addData = async (todoTitle) => {
	const url = "/addtodo/";
	const body = { title: todoTitle };
	try {
		const res = await axios_instance.post(url, body);
		return res.data ? res.data : null;
	} catch (err) {
		return { data: null, error: err.message ? err.message : "Not connected to the server" };
	}
};
