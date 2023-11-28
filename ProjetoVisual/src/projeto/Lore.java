package projeto;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;

import projeto.champions.Champions;

import javax.swing.JTextArea;
import javax.swing.JScrollBar;
import javax.swing.JScrollPane;
import javax.swing.JLabel;
import java.awt.Font;
import javax.swing.JButton;
import java.awt.Color;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class Lore extends JFrame {

	private static final long serialVersionUID = 1L;
	private JPanel contentPane;
	private Champions ch;
	private JTextArea txtLore;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Lore frame = new Lore();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public Lore() {
		
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 674, 462);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JScrollPane scrollPane = new JScrollPane();
		scrollPane.setBounds(10, 11, 638, 355);
		contentPane.add(scrollPane);
		
		txtLore = new JTextArea();
		txtLore.setFont(new Font("Tahoma", Font.PLAIN, 16));
		txtLore.setEditable(false);
		scrollPane.setViewportView(txtLore);
		txtLore.setLineWrap(true);
		txtLore.setWrapStyleWord(true);
		
		JButton btnNewButton = new JButton("Quiz");
		btnNewButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				Quiz frame = new Quiz(); 
				frame.setTitle(ch.getNome() + " / quiz");
				frame.setVisible(true);
				frame.Ch(ch);
				
				dispose();
			}
		});
		btnNewButton.setForeground(new Color(0, 0, 255));
		btnNewButton.setFont(new Font("Tahoma", Font.BOLD, 20));
		btnNewButton.setBounds(329, 377, 319, 35);
		contentPane.add(btnNewButton);
		
		JButton btnNewButton_1 = new JButton("Voltar");
		btnNewButton_1.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				HL HLframe = new HL();
				HLframe.Ch(ch);
				HLframe.setTitle(ch.getNome());
				HLframe.setVisible(true);
				
				dispose();
			}
		});
		btnNewButton_1.setFont(new Font("Tahoma", Font.BOLD, 20));
		btnNewButton_1.setBounds(10, 377, 319, 35);
		contentPane.add(btnNewButton_1);
		
	}
	
	public void Ch(Champions ch) {
		this.ch = ch;
		txtLore.setText(ch.getLore().replace("\n", "\n\n"));
	}
}
