import { useNavigate } from 'react-router-dom';

export const ErrorPage = () => {
    const navigate = useNavigate();
    return (
        <div className="w-full h-screen">
            <main className="relative isolate min-h-full">
                <img
                    alt=""
                    src="https://images.unsplash.com/photo-1545972154-9bb223aac798?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=3050&q=80&exp=8&con=-15&sat=-75"
                    className="absolute inset-0 -z-10 h-full w-full object-cover object-top"
                />
                <div className="mx-auto max-w-7xl px-6 py-32 text-center sm:py-40 lg:px-8">
                    <p className="text-base/8 font-semibold text-white">404</p>
                    <h1 className="mt-4 text-balance text-5xl font-semibold tracking-tight text-white sm:text-7xl">
                        Page not found
                    </h1>
                    <p className="mt-6 text-pretty text-lg font-medium text-white/70 sm:text-xl/8">
                        Sorry, we couldn’t find the page you’re looking for.
                    </p>
                    <div className="mt-10 flex justify-center">
                        <div
                            className="text-lg text-gray-200 font-semibold p-2 border-2 rounded-xl cursor-pointer hover:text-sky-500"
                            onClick={() => navigate('/')}
                        >
                            back to home
                        </div>
                    </div>
                </div>
            </main>
        </div>
    );
};