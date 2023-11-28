package projeto.champions;

import projeto.champions.quiz.Quiz;

public class Lux extends Champions{
	
	@Override
	public String getNome() {
		return "Lux";
	}
	
	@Override
	public String getP() {
		return "ILUMINAÇÃO\nAs habilidades de dano de Lux carregam o alvo com energia por alguns segundos. O próximo ataque de Lux incendeia a energia, causando Dano Mágico adicional (com base no nível de Lux) ao alvo.";
	}
	
	@Override
	public String getQ() {
		return "LIGAÇÃO DA LUZ\nLux atira uma esfera de luz que se prende e causa dano em até duas unidades inimigas.";
	}
	
	@Override
	public String getW() {
		return "BARREIRA PRISMÁTICA\nLux lança sua varinha e uma luz envolve todos os aliados atingidos, protegendo-os contra dano inimigo.";
	}
	
	@Override
	public String getE() {
		return "SINGULARIDADE LUCENTE\nDispara uma luz irregular em uma área, reduzindo a velocidade de inimigos próximos. Lux pode detoná-la para causar dano aos inimigos na área de ação.";
	}
	
	@Override
	public String getR() {
		return "CENTELHA FINAL\nApós acumular energia, Lux dispara um feixe de luz que causa dano a todos os inimigos na área. Além disso, ativa a habilidade passiva de Lux e reinicia a duração do efeito de Iluminação.";
	}
	
	@Override
	public String getLore() {
		return "O terremoto devastou a cidade de Terbisia, deixando-a em ruínas. Lux, uma demaciana, cavalga por entre os destroços em seu cavalo Fogo Solar, testemunhando a destruição. Ela se dirige a uma enfermaria improvisada para ajudar os feridos. Lux encontra o cirurgião Alzar e se oferece para ajudar como pode.\n"
				+ "Ao explorar o local, Lux encontra Dothan, um soldado gravemente ferido. Ele havia resgatado uma família dos escombros antes de ser atingido por um segundo terremoto, resultando em ferimentos fatais. Lux decide ficar ao lado de Dothan para confortá-lo em seus últimos momentos. Dothan, que perdeu a visão devido aos ferimentos, revela seu desejo de ver a luz de Demacia uma última vez.";
	}
	
	/*
	 * O terremoto devastou a cidade de Terbisia, deixando-a em ruínas. 
	 * Lux, uma demaciana, cavalga por entre os destroços em seu cavalo Fogo Solar, testemunhando a destruição. 
	 * Ela se dirige a uma enfermaria improvisada para ajudar os feridos. 
	 * Lux encontra o cirurgião Alzar e se oferece para ajudar como pode.
	 * 
	 * Ao explorar o local, Lux encontra Dothan, um soldado gravemente ferido. 
	 * Ele havia resgatado uma família dos escombros antes de ser atingido por um segundo terremoto, resultando em ferimentos fatais. 
	 * Lux decide ficar ao lado de Dothan para confortá-lo em seus últimos momentos. 
	 * Dothan, que perdeu a visão devido aos ferimentos, revela seu desejo de ver a luz de Demacia uma última vez.
	 */
	
	@Override
	public Quiz[] getQuiz() {
		Quiz[] quizes = new Quiz[4];		
		/*
		 * Pergunta 1: Por que Lux foi para a enfermaria improvisada após o terremoto?
		 * 	Para encontrar o cirurgião Alzar.
		 * 	Para procurar por sobreviventes nos destroços.
		 * Resposta correta: Para encontrar o cirurgião Alzar.
		 * 
		 * Pergunta 2: Qual foi o desejo final de Dothan antes de sua morte iminente?
		 * 	Desejava vingar-se dos responsáveis pelo terremoto.
		 * 	Desejava ver a luz de Demacia uma última vez.
		 * Resposta correta: Desejava ver a luz de Demacia uma última vez.
		 * 
		 * Pergunta 3: Como Lux ajudou Dothan nos seus últimos momentos?
		 * 	Curando suas feridas com magia.
		 * 	Criando uma luminosidade divina para que ele visse a luz de Demacia.
		 * Resposta correta: Criando uma luminosidade divina para que ele visse a luz de Demacia.
		 * 
		 * Pergunta 4: Qual foi o motivo dos ferimentos fatais de Dothan?
		 * 	Ele foi atingido por uma explosão mágica durante o terremoto.
		 * 	Um segundo terremoto causou a queda de destroços sobre ele.
		 * Resposta correta: Um segundo terremoto causou a queda de destroços sobre ele.
		 */
		
		String[] p1 = {"Para encontrar o cirurgião Alzar.", "Para procurar por sobreviventes nos destroços."};
		Quiz quiz = new Quiz("Por que Lux foi para a enfermaria improvisada após o terremoto?", "Para encontrar o cirurgião Alzar.", p1, 5);
		quizes[0] = quiz;
		String[] p2 = {"Desejava vingar-se dos responsáveis pelo terremoto.", "Desejava ver a luz de Demacia uma última vez."};
		quiz = new Quiz("Qual foi o desejo final de Dothan antes de sua morte iminente?", "Desejava ver a luz de Demacia uma última vez.", p2, 5);
		quizes[1] = quiz;
		String[] p3 = {"Curando suas feridas com magia.", "Criando uma luminosidade divina para que ele visse a luz de Demacia."};
		quiz = new Quiz("Como Lux ajudou Dothan nos seus últimos momentos?", "Criando uma luminosidade divina para que ele visse a luz de Demacia.", p3, 5);
		quizes[2] = quiz;
		String[] p4 = {"Ele foi atingido por uma explosão mágica durante o terremoto.", "Um segundo terremoto causou a queda de destroços sobre ele."};
		quiz = new Quiz("Qual foi o motivo dos ferimentos fatais de Dothan?", "Um segundo terremoto causou a queda de destroços sobre ele.", p4, 5);
		quizes[3] = quiz;
		
		return quizes;
	}
	
}
