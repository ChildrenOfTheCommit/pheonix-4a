<template>
	<div class="min-h-screen flex flex-col bg-linear-to-br from-purple-50 via-white to-indigo-50 animate-fade-in">
		<header class="fixed top-0 left-0 right-0 z-50 backdrop-blur-md border-b border-purple-100/50">
			<div class="container mx-auto px-6">
				<div class="max-w-6xl mx-auto flex items-center justify-between py-4">
					<div class="flex items-center gap-3 group cursor-pointer">
						<span class="text-2xl font-bold bg-linear-to-r from-purple-700 to-indigo-600 bg-clip-text text-transparent group-hover:from-purple-600 group-hover:to-indigo-500 transition-all duration-300">
							Alpha Centauri
						</span>
					</div>
					<router-link
							to="/login"
							class="px-8 py-3 bg-linear-to-r from-purple-600 to-indigo-500 text-white font-semibold rounded-full hover:shadow-xl hover:shadow-purple-500/40 hover:scale-105 transition-all duration-300 ease-in-out">
						Launch
					</router-link>
				</div>
			</div>
		</header>

		<main class="flex-1 flex items-center min-h-screen pt-24 pb-12">
			<div class="container mx-auto px-6">
				<div class="max-w-6xl mx-auto">
					<div class="grid lg:grid-cols-2 gap-16 items-center">
						<div class="space-y-6 order-2 lg:order-1 text-center lg:text-left">
							<h1 class="text-4xl md:text-5xl lg:text-6xl font-extrabold leading-tight">
								<span class="text-gray-800">Interstellar</span>
								<br>
								<span class="bg-linear-to-r from-purple-600 to-indigo-500 bg-clip-text text-transparent">Exploration</span>
								<span class="text-gray-800"> Management</span>
							</h1>
							<p class="text-xl text-purple-600 font-semibold">
								Year 2247 • IEA Command Center
							</p>
							<p class="text-gray-600 leading-relaxed max-w-lg mx-auto lg:mx-0 text-base">
								A centralized platform for explorers to record newly discovered planets across the galaxy.
								Commanders oversee the database and ensure the accuracy of all recorded information.
							</p>
							<div class="flex flex-wrap gap-3 justify-center lg:justify-start pt-2">
								<span class="px-4 py-2 bg-purple-100 text-purple-700 rounded-full text-sm font-medium border border-purple-200">
									<i class="fas fa-user-astronaut mr-2"></i>Explorers
								</span>
								<span class="px-4 py-2 bg-indigo-100 text-indigo-700 rounded-full text-sm font-medium border border-indigo-200">
									<i class="fas fa-crown mr-2"></i>Commanders
								</span>
								<span class="px-4 py-2 bg-purple-100 text-purple-700 rounded-full text-sm font-medium border border-purple-200">
									<i class="fas fa-star mr-2"></i>Discoveries
								</span>
							</div>
						</div>

						<div class="order-1 lg:order-2 flex justify-center">
							<div class="relative">
								<div class="absolute -top-10 -right-10 w-48 h-48 bg-purple-200/30 rounded-full blur-3xl"></div>
								<div class="absolute -bottom-10 -left-10 w-48 h-48 bg-indigo-200/30 rounded-full blur-3xl"></div>
								<img src="/favicon.png"
								     alt="Alpha Centauri"
								     class="w-72 h-72 object-contain animate-float drop-shadow-2xl">
							</div>
						</div>
					</div>
				</div>
			</div>
		</main>

		<footer class="bg-white/50 backdrop-blur-sm border-t border-purple-100/50">
			<div class="container mx-auto px-6">
				<div class="max-w-6xl mx-auto py-6 text-center text-sm text-gray-500">
					© 2247
					<a href="https://github.com/ChildrenOfTheCommit"
					   target="_blank"
					   rel="noopener noreferrer"
					   class="text-purple-600 font-medium hover:text-purple-700 transition-colors">
						Interstellar Exploration Agency
					</a>
					. All Rights Reserved.
				</div>
			</div>
		</footer>
	</div>
</template>

<style scoped>
@keyframes float {
	0%, 100% {
		transform: translateY(0px);
	}
	50% {
		transform: translateY(-16px);
	}
}

@keyframes fadeIn {
	from {
		opacity: 0;
		transform: translateY(20px);
	}
	to {
		opacity: 1;
		transform: translateY(0);
	}
}

.animate-float {
	animation: float 5s ease-in-out infinite;
}

.animate-fade-in {
	animation: fadeIn 0.8s ease-out;
}
</style>